import re

STOP_WORDS = {
    "a", "an", "and", "as", "at", "be", "by", "during", "for", "in", "is",
    "of", "on", "or", "the", "to",
}


def judge(question: str, expects: str, answer: str, results: str) -> bool:
    """
    Judge the answer against the correct answer.

    Args:
        answer (str): The answer provided by the user.
        correct_answer (str): The correct answer to compare against.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    # print(f"Question: {question}")
    # print(f"Expected: {expects}")
    # print(f"Answer: {answer}")
    # print(f"Results: {results}")
    # return False

    if not expects or not answer:
        return False

    expected_tokens = [
        token
        for token in re.findall(r"\$?\d+(?:\.\d+)?|[a-z]+", expects.lower())
        if token not in STOP_WORDS
    ]
    answer_tokens = set(re.findall(r"\$?\d+(?:\.\d+)?|[a-z]+", answer.lower()))
    return all(token in answer_tokens for token in expected_tokens)