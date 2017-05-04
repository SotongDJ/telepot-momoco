echo "sh daemon.sh"
echo "    pkill python"
pkill -e python
echo "    python3 daemon.py"
python3.4 daemon.py #>> database/opt/bot.log
echo "daemon.sh close"
