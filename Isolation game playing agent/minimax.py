def minimax_decision(gamestate,depth):
	best_score = float('-inf')
	best_move = None
	for m in gamestate.get_legal_moves():
		v = min_value(gamestate.forecast_move(m),depth - 1)
		if v>best_score:
			best_score = v
			best_move = m
	return best_move

def min_value(gamestate,depth):
	if(terminal_test(gamestate)):
		return(1)
	if(depth<=0):
		return(0)

	v=float('inf')	
	for m in gamestate.get_legal_moves():
		v = min(v,max_value(gamestate.forecast_move(m),depth-1))
	return(v)	

def max_value(gamestate,depth):
	if(terminal_test(gamestate)):
		return(-1)
	if(depth<=0):
		return(0)
	v=float("-inf")
	for m in gamestate.get_legal_moves():
		v = max(v,min_value(gamestate.forecast_move(m),depth-1))
	return(v)

call_counter = 0

def terminal_test(gameState):
    global call_counter
    call_counter += 1
    moves_available = bool(gameState.get_legal_moves())  # by Assumption 1
    return not moves_available

		



