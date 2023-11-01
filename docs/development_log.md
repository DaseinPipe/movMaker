Here we maintain a running log of our discussions, decisions, and milestones. 

Date: 04/10/23

    Discussed the structure and modules of the tool.
    Set up the documentation structure in the repository.
    Planned to delve into user persona and journey in the next discussion.

    31/10/23

    A rejig to the repo dir and file structure
    refining thoughts on responsibilities, accountability
    
    ### NEW REPO LAYOUT AND HEADERS ###
    
        src/: The main components of our application.

        managers/: Responsible for management and orchestration logic.
            config_manager.py: Deals with configuration loading and validation.
            image_sequence_loader.py: Loads image sequences based on configuration.
            pipeline_manager.py: Orchestrates the entire flow of the application.
            raster_processing_manager.py: Orchestrates the image processing flow.

        raster_plugins/: Handles the image processing logic.
            oiiotool_processor.py: The specific implementation using oiiotool.
            slate_generator.py: Generates slates for videos.
            text_renderer.py: Renders text onto images.

        pyutils/: Contains shared utility functions or classes.
            validation_utils.py: Contains validation functions.
            file_utils.py: Directory and file searching functions.
            csv_utils.py: CSV processing functions.
            ... (Additional utility files as required)

        exceptions/: (Optional) For custom exceptions.
            custom_exceptions.py: Custom exceptions for the application.

    data/: Configuration and other data-related files.
        configs/: Configuration files that the application uses.

    tests/: (Optional) For automated testing.
        test_config_manager.py: Test cases for the config manager.
        ... (Additional test files as required)

    main.py: Entry point for the application.


Date 31/10/23

Sequence loader steps:

0 - go to parent directory as supplied
1 - extension
2 - period ahead of the extension must have an integer to its left otherwise discard
3 - next period left of the first and only integers separateing them, chuck anything with non-integer chars (that includes spaces and also nothing, ie "..ext")
4 - padding - no sorting, this just throws away non-matching padded numbers
5 - filename - start with first and simply iterate through to the first period, throw anything left away

This method guarantees you only use the provided information at all times. Each of the steps is self-reliant. It matters not which order they're done. They're all needed but not necessarily all used. If there are no files then it fails at the first hurdle - without even needing to add a check for empty directory even! If there are no matching extensions then it exits immediately. Think of these as a set of rules for rejecting files not for finding sequences.
These steps are done at the micro level, not macro. They do not pass information along because their information would be utterly useless to the next step.


The csv data is brought without prejudice!
I'm going to ask that there be No Dictionaries used during these steps. Blind/raw/unformatted filename caches only, 


0 - go to parent directory as supplied - PASS or FAIL

1 - extension - FIND MATCHING EXT AND DISPOSE OF THE REST ***this can't shortcutted to a find only, we must have the ability to harvest the discarded data***

2 - period ahead of the extension must have an integer to its left otherwise discard - ITERATE THROUGH EACH FILE ***this can't shortcutted to a find, we should have the ability to harvest the discarded data ***

3 - next period left of the first and only integers separateing them, chuck anything with non-integer chars (that includes spaces and also nothing, ie "..ext") - IT'S VITAL THAT THERE BE NO "." TO THE LEFT OF THE SECOND ONE just as it's vital there be only integers separating the first and second ***this can't shortcutted to a find, we must have the ability to harvest the discarded data!!***

4 - padding - THIS ISN'T AS SIMPLE AS COUNTING HOW MANY INTEGERS THERE ARE but if it'll me straightforward to add the proper check later then ok to do a simple count now ***we'll want the rejected data***

5 - filename - start with first and simply iterate through to the first period, throw anything left away - BECAUSE WE'VE DONE THE 5 PREVIOUS STEPS IT'S POSSIBLE FOR US TO CHECK EACH FILE FOR MATCHING START ***BUT WE MUST ADD A SECOND STEP FOR MATCHES WHICH LOOKS FOR A "." directly after the matched name - there NO NEED TO CHECK FOR ANYTHING BUT A ".", if it's missing the file is DUMPED BECAUSE IT'S NOT VALID***

Remember - No Dictionaries




Image Processing Phase:

Image adjustments using OiiotoolProcessor.
Sequence Validation: Ensure all frames in a sequence are present and in the correct order.
Sequence Repair (if necessary): Retrieve missing frames or generate placeholders.
Log any discrepancies or actions taken.
Encoding Phase:

Since the sequence is already validated, you can directly proceed to encoding.
Use ffmpeg to encode the sequence into a video.
Log the encoding process and any issues encountered.