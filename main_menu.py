# pylint: disable=C0111,W0401,W0614
import re
import branches
from Messages import *
from User import *
from NewSettings import *


class main_menu:

    def __init__(self, bot):
        self.branches = branches.get_branches()
        self.bot = bot
        self.current_users = {}

    def _get_reaction(self, message, callback):
        if message:
            message = Message(message=message)
        elif callback:
            message = Message(callback=callback)
        else:
            return 0

        user, status = self.get_user(message)
        return message, user, status

    def get_reaction(self, message=None, callback=None):
        message, user, status = self._get_reaction(message, callback)
        branch = user.branch
        current_branch = self.branches[branch]['steps']
        if status == NEW_STATUS:
            current_branch[0].on_call(self, user, message)
        elif status == OLD_STATUS:
            if message.is_backbutton():
                if user.phase != 0:
                    user.phase -= 1
                cur_phase_num = user.get_phase()
                user = current_branch[cur_phase_num].on_undo(
                    self, user, message)
                self.set_user(user)

                current_branch[cur_phase_num].on_call(self, user, message)
            elif message.is_nan():
                return 0
            else:
                cur_phase_num = user.phase
                step = current_branch[cur_phase_num]
                if step.check_access(self, user, message):
                    user, next_step = step.on_return(self, user, message)
                    if next_step == 'NEXT':
                        user.phase += 1
                        next_step = cur_phase_num + 1
                    elif next_step == 'CURRENT':
                        user.phase = user.phase
                        next_step = user.phase
                    elif next_step == 'OVER':
                        user.phase = len(current_branch) - 3
                        next_step = user.phase
                    elif next_step == 'PREVIOUS':
                        user.phase -= 1
                        next_step = user.phase

                    current_branch[next_step].on_call(self, user, message)
                else:
                    self.error_message(message)

    def get_user(self, message):
        user_id = message.user_id
        return_data = (None, None)
        if user_id in self.current_users:
            restart_commands = [self.branches[k]['restarts']
                                for k in self.branches]
            for pos, restarts in enumerate(restart_commands):
                for cmd in restarts:
                    if re.findall(cmd, message.content):
                        branch_key = list(self.branches.keys())[pos]
                        kwargs = self.branches[branch_key]['start'](message)
                        kwargs['branch'] = branch_key
                        user = User(user_id, message.id, branch_info=kwargs)
                        self.current_users[user_id] = user
                        return user, NEW_STATUS

            return self.current_users[user_id], OLD_STATUS
        else:
            trigger_commands = [self.branches[k]['triggers']
                                for k in self.branches]
            for pos, triggers in enumerate(trigger_commands):
                for cmd in triggers:
                    if re.findall(cmd, message.content):
                        branch_key = list(self.branches.keys())[pos]
                        kwargs = self.branches[branch_key]['start'](message)
                        kwargs['branch'] = branch_key
                        kwargs['last_message_content'] = message.content
                        user = User(user_id, message.id, branch_info=kwargs)
                        self.current_users[user_id] = user
                        return user, NEW_STATUS
            if return_data == (None, None):
                print(f'There is no branch for this message:\n"{message.content}"')

    def update_users(self, user_id, user):
        self.current_users[user_id] = user

    def error_message(self, message):
        if message.type == 'message':
            text = 'Воспользуйтесь кнопками меню выше'
            self.bot.reply_to(message.message, text)

    def set_user(self, user):
        user_id = user.id
        self.current_users[user_id] = user
