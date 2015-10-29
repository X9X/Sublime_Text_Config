import sublime, sublime_plugin
import webbrowser
import os
 
url_map = {
     'D:\yang\www\mysite' : 'http://localhost',
}
 
class OpenBrowserCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        window = sublime.active_window()
        window.run_command('save')
        url = self.view.file_name()
        flag = False
        for path, domain in url_map.items():
            if url.startswith(path):
                url = url.replace(path, domain).replace('\\', '\/')
                flag = True
                break
        if not flag:
            url = url
            # url ='/root/a.txt'
        # webbrowser.get('firefox').open(url)
        # webbrowser.get('firefox')
        # url = "http://www.baidu.com"
        webbrowser.open_new(url)
        # web = "C:/Program Files/Mozilla Firefox/firefox.exe"
        # url = "http://baidu.com"
        # os.system('"C:/Program Files/Mozilla Firefox/firefox.exe" '+url)
        # os.system("%s %s %s"%(web,url))