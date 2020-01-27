# assert statement

'''
assert statement says that apart from all the rules,
a particular condition should always be true,
to make sure there is no bug in the code
and if  not then raise an exception.
'''

def switchLights(trf_inter):     #parameter is traffic_intersection
    for key in trf_inter.keys():
        if trf_inter[key] =='green':
            trf_inter[key] = 'yellow'
        elif trf_inter[key] =='yellow':
            trf_inter[key] = 'red'
        elif trf_inter[key] =='red':
            trf_inter[key] = 'green'
            
    assert_message = '''Neither light is red!!!
                        Traffic will flow in all direction and can cause accident.'''
                                
    assert_message = " ".join(assert_message.split())
    assert 'red' in trf_inter.values(),  assert_message+'\n'+ str(station_market)
        


station_market = {'for_back' : 'green', 'left_right' : 'red'}
print(station_market)
switchLights(station_market)
print(station_market)



