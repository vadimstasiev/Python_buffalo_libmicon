#!/bin/sh
export message_line_1
export message_line_2
export status

backup_failed="false"

push_message(){
        echo_messages
        python3 LCD_message.py
}

echo_messages(){
        echo $message_line_1
        echo $message_line_2
}

if ps -ef | grep -v grep | grep rsync; then
        echo "Rsync already running... Backup Cancelled."
        exit 0
else
        for value in srv01-storage \
                        srv01-fam \
                        srv01-david \
                        vadim \
                        anatolie
        do
                if mountpoint -q "/media/${value}/"; then
                        message_line_1="Rsync running..."
                        message_line_2=$value
                        status="busy"
                        push_message
                        sleep 5
                        # rsync -S -vrltH -pgo --stats -D --numeric-ids --delete --partial --progress --exclude="#snapshot" --exclude="#recycle" /media/$value/ /media/hdd/backups/$value
                        message_line_1="Rsync complete"
                        message_line_2=$value
                        status="done"
                        push_message
                else
                        message_line_1 = "Error Not mounted"
                        message_line_2 = $value
                        status="error"
                        backup_failed="true"
                        push_message
                fi
                sleep 60
        done
fi
if [ "$backup_failed" = "true" ]
then
        message_line_1="Backup Error"
        status="error"
else 
        message_line_1="Last Rsync"
        status="done"
fi
message_line_2=$(date +'%d/%m/%y-%H:%M')
push_message
