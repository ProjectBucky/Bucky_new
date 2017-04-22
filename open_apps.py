import subprocess

def open_app(app_name):
	subprocess.call(app_name)
if __name__=="__main__":
	open_app("explorer c:")