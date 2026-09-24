def judge(question: str, expects: str, answer: str, results: str) -> bool :
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

    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()