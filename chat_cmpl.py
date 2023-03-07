import keyboard as kb
import requests as r
import ui
import sseclient
import json
import sys

OPENAI_TOKEN = "REPLACE_WITH_YOUR_TOKEN"

def cmpl(prompt):
	resp = r.post("https://api.openai.com/v1/chat/completions", verify=False, stream=True, json={
		"model": "gpt-3.5-turbo",
		"messages": [{
			"role": "user",
			"content": prompt
		}],
		"stream": True
	}, headers={
		"Accept": "text/event-stream",
		"Authorization": f"Bearer {OPENAI_TOKEN}"
	})
	
	client = sseclient.SSEClient(resp)
	return client

class ChatCmplView(ui.View):
	def __init__(self, *args, **kwargs):
		ui.View.__init__(self, *args, **kwargs)
	
	def did_load(self):
		self["btn_stop"].action = self.stop
	
	def stop(self):
		self.stop()
		sys.exit(0)

def extract_msg_delta(resp):
	choices = resp["choices"]
	if len(choices) >= 1:
		first = choices[0]["delta"]
		if "content" in first:
			return first["content"]
	
	return ""
		
	
def main():
	if kb.is_keyboard():
		v = ui.load_view('ChatCmplView.pyui')
		kb.set_view(v, 'minimized')
		
		pmpt = kb.get_input_context()[0]
		selected = kb.get_selected_text()
		if selected.strip() != "":
			pmpt = selected
		cli = cmpl(pmpt)
		
		v["status"].text = "Completing... (0)"
		
		total = 0
		
		for event in cli.events():
			if event.data != "[DONE]":
				msg = extract_msg_delta(json.loads(event.data))
				total += len(msg)
				v["status"].text = f"Completing... ({total})"
				
				kb.insert_text(msg)
			else:
				v["status"].text = f"Completion Finished ({total})"
				def animate():
					v["btn_stop"].alpha = 0.0
				ui.animate(animate, duration=0.2)
	else:
		cli = cmpl("Hello")
		
		for event in cli.events():
			if event.data != "[DONE]":
				print(extract_msg_delta(json.loads(event.data)), end="", flush=True)

if __name__ == '__main__':
	main()