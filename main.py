def euler(a,b, X_0, num_steps, t_0, t_f, num_simulations = 1000, ant_variates = False): 
    delta_t = (t_f - t_0)/num_steps 

    S = np.zeros((num_simulations, num_steps +1))
    W = np.random.normal(0,1,(num_simulations, num_steps)) 

    for i in range(num_simulations):
        S[i,0] = X_0 

    
    if ant_variates: 
        ant_S = S
    
    for i in range(num_simulations):
        for j in range(num_steps): 
            t = t_0 + delta_t*j 
            
            deterministic_term = a(S[i,j], t)*delta_t 
            random_term        = b(S[i,j], t)*(math.sqrt(delta_t)*W[i,j]) 
            if ant_variates: 
                ant_deterministic_term = a(ant_S[i,j], t)*delta_t 
                ant_random_term        = b(ant_S[i,j], t)*(-math.sqrt(delta_t)* W[i,j])

            S[i,j+1] = S[i,j] + deterministic_term + random_term 
            if ant_variates: 
                ant_S[i,j+1] = ant_S[i,j] + ant_deterministic_term + ant_random_term
    return S 
