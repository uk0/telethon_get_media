#!/bin/bash
for ((;;)) do 
status=$(ps -ef | grep main.py | grep -v 'grep' |grep -v 'du*' | wc -l);
echo $status;  
if [ $status -eq 0 ]
then
    echo "nohup python main.py &"
	    nohup python main.py &
		    sleep 15 ;
			else
			    echo "py is running"
				fi

				 sleep 3 ; 
				  done
