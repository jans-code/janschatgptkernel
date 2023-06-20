##!/usr/bin/env python
import os
import openai
from ipykernel.kernelbase import Kernel

openai.api_key = os.getenv("OPENAI_API_KEY")

class janschatgptkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'ChatGPT'
    language_version = '3.5'
    language_info = {
        'name': 'ChatGPT',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "ChatGPT by OpenAI"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": code}
                ]
            )
            solution = completion.choices[0].message.content
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
