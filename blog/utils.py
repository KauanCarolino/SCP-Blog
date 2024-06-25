

def show_results_filter_set(qr):
    query_params = set(qr.keys())
    if ((len(query_params) == 1 and 'iframe' in query_params) or
            len(query_params) == 0):
        return False

    return True