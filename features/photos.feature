Feature: Photo Grid
    Scenario: viewing all the photos uploaded to Timor Journey
        When we visit Timor Journey
        Then we should see the app is loading photos
        Then we should see many photos in a grid
    
    Scenario: seeing the photo larger
        When we visit Timor Journey
        And we click on a photo card
        And we click on the viewer card
        Then we see the photo viewer