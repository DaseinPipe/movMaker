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