import sublime_plugin
import os
import platform

class ImeoffCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if platform.system()!="Windows":
            cmd = """
            osascript -e 'tell application "System Events" to key code {102}'
            """
            os.system(cmd)

        self.view.run_command('exit_insert_mode')
