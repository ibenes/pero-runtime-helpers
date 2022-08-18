if [ nvidia-smi ] 
then
    :  # a NOP to avoid syntax error
else
    send-mail.py \
        -f 'pero@fit.vutbr.cz'
        -t 'ibenes@fit.vutbr.cz' \
        -s 'GPU check' \
        -c "GPU check on $(hostname) failed" \
        >> ~/send-mail.txt
fi
