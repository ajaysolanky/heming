from llm_functions import openai_call, claude_call


REVIEW_PROMPT_TEMPLATE = """
Can you tell me what changes you would make to this passage in order to modify the text, according to the instructions?

instruction: {instruction}
passage: {passage}

Make concrete recommendations via inserts and deletes.
So return the original text but:
If you want to delete a portion, surround it by the tags "<delete>" and "</delete>"
If you want to insert some text, surround it by the tags "<insert>" and "</insert>"

I will use a compiler to compile this down to text that shows the modifications, sort of how you can track  modifications in google docs

For example, if I provided you with this:

instruction: rewrite this passage with much more flowery language
passage: Janice looked nice. In her left hand, she held a rose.

Response:
Janice looked <delete>nice</delete><insert>stunning beyond compare</insert>. In her left hand, she <delete>held a rose</delete><insert>gripped a scarlet, scintillating rose</insert>.

Make sure that the resulting passage after suggested modifications is properly written and well constructed.

Response:"""

def get_passage_edits(instruction, passage, model):
    llm_prompt = REVIEW_PROMPT_TEMPLATE.format(
        instruction=instruction,
        passage=passage
    )
    messages = [{"role": "user", "content": llm_prompt}]
    if model == 'openai':
        return openai_call(messages)
    elif model == 'claude':
        return claude_call(messages)

