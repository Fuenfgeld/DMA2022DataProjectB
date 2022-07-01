sudo apt install sqlite3

DIR="DMA2022DataProjectB"
if [ -d "$DIR" ]; then
    ### Take action if $DIR exists ###
    echo "Error: ${DIR} already exists."
else
  ###  Control will jump here if $DIR does NOT exists ###
    echo "Installing config files in ${DIR}..."
    git clone https://github.com/Fuenfgeld/DMA2022DataProjectB.git
  
  exit 1
fi
