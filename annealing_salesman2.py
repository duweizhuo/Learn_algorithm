tmp = 1e3
tmp_min = 1e-5
alpha = 0.99
s_old = dist(cities1)
cit_new = cities1
s_new = s_old

while(tmp > tmp_min):
    cit_new = new_solve(cities1)
    s_new = dist(cit_new)
    dE = (s_new-s_old) * 500
    
    if(dE > tmp):
        cities1 = cit_new
        s_old = s_new
        
    if(dE < 0):
        counter = 0
        tmp = tmp * alpha
    else:
        counter = counter + 1
        
    if(counter > 1e4):
        break
def draw-route(in):
def dist():
    
