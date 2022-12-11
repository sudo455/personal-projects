
ssh-keygen

echo "start ssh-agent"
eval $(ssh-agent -s)

echo "give me the name of the ssh key that you created"
read ssh_name
ssh-add /home/$(whoami)/.ssh/${ssh_name}

echo "that's all now you have the ${ssh_name}"e