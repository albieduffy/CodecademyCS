# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def learning_censor(email):
  return email.replace('learning algorithms', '----------------')

def list_censor(email):
    for term in proprietary_terms:
        email = email.replace(term, '-' * len(term))
    return email

# def negative_censor(email):
#     email_temp = ''
#     first_instance = []
#     for word in email:
#         if word in negative_words:
#             if word in first_instance:
#                 email_temp += '-----'
#             else:
#                 first_instance.append(word)
#                 email_temp += word
#         else:
#             email_temp += word

# def all_censor(email):
#     return True
