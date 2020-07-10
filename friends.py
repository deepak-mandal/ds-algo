

def food(f, num):
    '''Take total no. of people as arguments'''
    tip=f*0.1         #--------------------------------------------------------calculate tip
    f=f+tip             #------------------------------------------------------add tips to total
    return f/num             #-------------------------------------------------return the per person vallue

def movie(m, num):
    '''Take total and no. of people as argument'''
    return m/num             #-------------------------------------------------Returns the per person value
