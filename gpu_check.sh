echo 'Running gpu check at ' $(date) >> ~/cron-test.txt

if [ nvidia-smi ] 
then
	:  # a NOP to avoid syntax error
else
	python3 /home/pero/restarting/send-mail.py \
		-t 'ibenes@fit.vutbr.cz' \
		-s 'GPU check' \
		-c 'GPU check failed' \
		>> ~/send-mail.txt
fi
