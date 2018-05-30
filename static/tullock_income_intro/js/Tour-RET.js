
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
        debug: false
    });

    tour.addSteps([
     {
        element: ".otree-timer",
        placement: "left",
        backdrop: true,
        title: "Time left in this round",
        content: "This timer shows you the time left in this round to either solve sequences or stay in 'Switch'"
      },
     {
        element: "#number_strings",
        placement: "left",
        backdrop: true,
        title: "Number of Sequences Solved",
        content: "This counter shows you how many sequences you have solved so far."
      },
      {
        element: "#switch_modal",
        placement: "right",
        title: "Switch Button",
        content: "By clicking this button you will enter the 'Switch' mode. You will need to confirm first. Once " +
        "you go into 'Switch' mode you cannot go back to the letter counting task!",
        duration: 10000
      }
    ]);

    // Initialize the tour
    tour.init();

    // Start the tour
    tour.start();

}());