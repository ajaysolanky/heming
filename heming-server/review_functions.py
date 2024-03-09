from llm_functions import openai_call, claude_call


REVIEW_PROMPT_TEMPLATE = """
Can you tell me what changes you would make to this passage in order to modify the text, according to the instructions?

instruction: {instruction}
passage: {passage}

Make concrete recommendations via inserts, deletes, and comments.
So return the original text but:
If you want to delete a portion, surround it by the tags "<delete>" and "</delete>"
If you want to insert some text, surround it by the tags "<insert>" and "</insert>"
If you want to leave a comment around a portion of text, surround the targeted portion by the tags <comment_n> and </comment_n> , where n is an integer.
At the bottom of the document, leave a line that looks like: [n]: ~the text of the comment you want to leave~
Comments should be higher level feedback about the structure and flow of the writing that cannot be communicated via direct modifications.

I will use a compiler to compile this down to text that shows the modifications, sort of how you can track  modifications in google docs

For example, if I provided you with this:

instruction: rewrite this passage with much more flowery language
passage: Janice looked nice. In her left hand, she held a rose.

RESPONSE:
<comment_1>Janice looked <delete>nice</delete></comment_1><insert>stunning beyond compare</insert>. <comment_2>In her left hand</comment_2>, she <delete>held a rose</delete><insert>gripped a scarlet, scintillating rose</insert>.
[1]: Remember that you should be looking to show, not tell
[2]: Maybe add some description of the hand

Make sure that the resulting passage after suggested modifications is properly written and well constructed.
Only leave comments if you think they will be particularly helpful. It is perfectly acceptable to leave 0 comments.
Only return the text of the response, no extra commentary.

RESPONSE:"""

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

