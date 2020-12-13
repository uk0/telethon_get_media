#!/bin/bash

basepath=$(cd `dirname $0`; pwd)

cd $basepath

cleanup (){
echo "kill main.py task.py"
ps -ef | grep -E 'main.py|task.py'| awk '{print$2}' | xargs kill -9
exit 0

}
# 监控信号量
trap cleanup SIGINT SIGTERM

#启动 task
nohup python task.py  2>&1 > /dev/null &

# 循环监控
for ((;;)) do
status=$(ps -ef | grep main.py | grep -v 'grep' |grep -v 'du*' | wc -l);
#echo $status;
if [ $status -eq 0 ]
then
echo "nohup python main.py &"
nohup python main.py &
sleep 15 ;
else
echo "get media is running"
fi

sleep 3 ;
done