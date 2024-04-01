# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "A record that meets the criteria of both being a Home Owner (yes) and having a Low Annual Income (yes) can fall under two distinct rules simultaneously, indicating that the rules are not mutually exclusive"
    answers["(b) explain"] = "The rules are incomplete as they do not cover cases where Marital Status is Divorced."
    answers["(c) explain"] = "Due to the overlap among the rules, prioritizing them and systematically organizing them is important. For instance, a scenario where an individual is not a homeowner (Home Owner = No) and is single (Marital Status = Single) would fit into two distinct rules within the established set of rules."
    answers["(d) explain"] = "A default class is necessary because a record with Marital Status = Divorced and Home Owner = No does not meet any of the specified rules."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "Considering the provided rules and dataset, no vertebrate qualifies for classification into more than one class, indicating that the rules are mutually exclusive."
    answers["(b) example"] = "Since the rules do not classify amphibians, the rules are not comprehensive."
    answers["(c) example"] = "Since there are no overlaps among the rules, sequencing them is not required."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The gradient of weights is determined through the chain rule, allowing the gradient of the (k+1)th weight to be computed based on the gradient of the kth weight during backpropagation, as the process moves from the output layer to the input layer."
    answers["(b) explain"] = "The activation in the (k+1)th layer node is the weighted sum of activations from the kth layer, enabling it to be utilized in the calculation."
    answers["(c) explain"] = "The described phenomenon is known as overfitting, not the vanishing gradient problem."
    answers["(d) explain"] = "The gradient of the loss will be zero if either the input is zero or the loss has reached a global minimum."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.32

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "For k=5, a balance is achieved, as k=1 treats each point as a separate cluster, while k=50 weakens the data's local structure."
    answers["(b) explain"] = "It takes into account a sufficient number of neighbors to discern local data patterns without being so few as to be excessively affected by noise."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "It selects an adequate number of neighbors to identify local patterns in the data, avoiding a count so low that it becomes overly susceptible to noise."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0  ## Verify

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "For the positive class, the Naive Bayes calculation yields 0.192 (by multiplying values from part a associated with the positive class), and for the negative class, it results in 0.032. Consequently, the positive class is the predicted outcome according to Naive Bayes."
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'no'

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "No, because the conditional probability P(X|YZ) = 0.5 differs from P(X|Z) = 0.6, where X represents (A=1), Y signifies (B=1), and Z stands for the positive class."
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    #answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    #answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
