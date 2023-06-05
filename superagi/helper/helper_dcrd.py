from superagi.tools.thinking.tools import LlmThinkingTool


def _execute(message) -> str:
    _input = message.lower()
    if _input != '' and _input != None and _input[:1] == "/":
        gpt = LlmThinkingTool()
        return gpt._execute(_input)

    