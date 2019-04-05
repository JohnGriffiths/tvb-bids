docker-build:
	docker build -t tvb-bids . 

shell: 

        docker run -v /c/Ubuntu_WSL/Code/libraries_of_mine/github/tvb-bids_data:/bids-dataset -it --entrypoint=bash tvb-bids

run:

        docker run -i --rm -v /c/Ubuntu_WSL/Code/libraries_of_mine/github/tvb-bids_data:/bids-dataset tvb-bids


