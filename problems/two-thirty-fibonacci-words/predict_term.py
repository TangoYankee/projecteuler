

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

# generate_sequence()
