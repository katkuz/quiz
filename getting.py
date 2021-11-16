def get_user_answers():
    """ Get answer(s) in text from console and parse them to a list.
    Multiple options answer expected to be separated by comma  """
    given_answers = list()
    try:
        given_answer_txt = input("Ditt svar: ").strip()  # strip in order to avoid "space" problem
        if "," in given_answer_txt:
            given_answers = [int(x.strip()) for x in
                             given_answer_txt.split(',')]  # strip in order to avoid "space" problem
        else:
            given_answers.append(int(given_answer_txt))
    except:
        pass
    return given_answers
