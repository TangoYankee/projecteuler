import re

def predict_term(index):
    '''
    test ability to predicted which term will appear next in the sequence
    '''
    even_double_pattern = [3,5,3,5,5]
    odd_double_pattern = [5,3,5,5,3]
    A = 'A'
    B = 'B'
    build_term = ''
    F = generate_sequence((index-1))
    generated_term = F[-1]
    print(f'length of term:  {len(generated_term)}')
    if is_even(index):
        for i in range(len(generated_term)):
            if i == 0:
                build_term += A
            elif i == 1:
                build_term += B
    return build_term

def is_even(value):
    remainder = value % 2
    if remainder == 0:
        return True
    else:
        return False

def generate_sequence(length):
    F = ['A', 'B']
    for i in range(length):
        term = F[i]+F[i+1]
        F.append(term)
    return(F)

def double_second():
    F = generate_sequence(20)
    term = F[-1]
    return ([m.start() for m in re.finditer('BB', term)])

def repeat_difference():
    double = double_second()
    differences = []
    for i in range(1, len(double)):
        difference = double[i]-double[i-1]
        differences.append(difference)
    return differences

def double_fives():
    differences = repeat_difference()
    five_streak_tracker = []
    five_streak_counter = 0
    for number in differences:
        if number == 5:
            five_streak_counter +=1
        else:
            five_streak_tracker.append(five_streak_counter)
            five_streak_counter = 0
    return(five_streak_tracker)

def double_double():
    differences = double_fives()
    two_streak_tracker = []
    two_streak_counter = 0
    for number in differences:
        if number == 2:
            two_streak_counter +=1
        else:
            two_streak_tracker.append(two_streak_counter)
            two_streak_counter = 0
    print(two_streak_tracker)

# generate_sequence()
# double_second()
# repeat_difference()
# double_fives()
double_double()