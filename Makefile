docker-build:
	docker build -t tvb-bids . 

run:
        docker run -i --rm -v /c/Ubuntu_WSL/Code/libraries_of_others/github:/github:ro tvb-bids demo_num


shell:
        docker run -v /c/Ubuntu_WSL/Code/libraries_of_others/github:/github:ro -it --entrypoint=bash tvb-bids demo_num


