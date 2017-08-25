#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:55:27 2017

@author: misakawa
"""

class Typedef:
    def __init__(self, type_, error_msg = "Type of argnument {idx} should {type}" ):
        self.type_     = type_
        self.error_msg = error_msg
    def set_lambda(self, dual_callable_obj):
        self.check = lambda input_var: dual_callable_obj(input_var, self.type_)

def _check(input_var, check_type, idx = None, key = None):
    if isinstance(check_type, Typedef):
        if not check_type.check(input_var):
            raise TypeError(check_type.error_msg.format(key = key, type = check_type.type_))
    else:
        if not isinstance(input_var, check_type):
            raise TypeError(f"Type of argnument {idx} should {check_type}")
            
class strict:
	@staticmethod
	def args(*typeargs : (*(),), **typekwargs:dict): 
	        def _1(func):
	            def _2(*args, **kwargs):
                    
	                for arg_idx, (arg,typearg) in enumerate(zip(args, typeargs)):
                        
                        try:
                            _check(arg, typearg)
                        except TypeError as e:
                            raise e
	                for key in kwargs:
                        try:
                            _check(kwargs[key], typekwargs[key])
                        except TypeError as e:
                            raise e
                            
	                return func(*args,**kwargs)
	            return _2
	        return _1
	    
	def ret(*typerets):
	        def _1(func):
	            def _2(*args, **kwargs):
	                ret = func(*args, **kwargs)
                    
	                if len(typerets) > 1:
	                    for ret_idx,(ret_i, typeret) in enumerate(zip(ret, typerets)):
                            try:
                                _check(ret_i, typeret)
                            except TypeError as e:
                                raise e
	                else:
                        try:
                            _check(ret, typerets[0])
                        except TypeError as e:
                            raise e
                            
	                return ret
	            return _2
	        return _1
