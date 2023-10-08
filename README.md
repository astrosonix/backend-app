# AstroSonix backend app

## Usage

For now, this app is not deploy anywhere and is serves as a proof of concept.

Installation:
1. `docker compose up --build`
2. `Go to http://localhost:8000` and follow instructions to generate unique tone

## Algorithm

Overview of the extended version of the algorithm (this is PoC)
can be found in our submission to SpaceApps Challenge.

In this PoC:
* we use API wrappers for LLM and open-sourced MusicLM model by Meta.
    * MusicLM model can be deployed locally but due to the time contained we decided to use online version
* we use OpenCV to utilize computer vision to assess image features and extract emotions
* We use FastAPI framework for setting up basic REST API
* We did not integrate this backend with our frontend yet. Both of them however in total provide a prototype of AstroSonix MVP.  
