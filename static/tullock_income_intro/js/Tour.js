
//this initiates the tooltip mouseover to explain the counters
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
//

$(function () {
  $('[data-toggle="popover"]').popover()
})



(function(){

    var tour = new Tour({
        storage : false,
        debug: true
    });

    tour.addSteps([
      {
        element: "#step_1",
        placement: "left",
        backdrop: true,
        title: "Time spent solving the current sequence",
        content: "This timer will show you how long you have spent trying to solve the current sequence. " +
        "Once you submit a correct answer, the timer will restart."
      },
      {
        element: "#string",
        placement: "left",
        backdrop: true,
        title: "Sequence",
        content: "This is the sequence of characters for which you have to count the number of 'a's."
      },
      {
        element: "#player_guess",
        placement: "left",
        title: "Solution",
        content: "Type here the number of 'a's in the sequence above and hit enter to submit.",
        duration: 10000
      }
    ]);

    // Initialize the tour
    tour.init();

    // Start the tour
    tour.start();

}());