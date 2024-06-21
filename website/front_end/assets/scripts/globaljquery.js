// Defining functions
function navToggle() {
    $(".hamburger").toggleClass("active");
    $(".nav-menu").toggleClass("active");
    $(".navbar").toggleClass("active");
};
function navCollaps() {
    $(".hamburger").removeClass("active");
    $(".nav-menu").removeClass("active");
    $(".navbar").removeClass("active");
};
function navActivationToggle() {
    var scrollPos = $(document).scrollTop();
    $('.nav-link').each(function () {
        var refElement = $($(this).attr("href").match("#.*$")[0]);
        if (refElement.length) {
            if (refElement.position().top <= (scrollPos + $(".navbar").outerHeight()) && refElement.position().top + refElement.outerHeight() > scrollPos + $(".navbar").outerHeight()) {
                $('.nav-link').removeClass("active");
                $(this).addClass("active");
            } else {
                $(this).removeClass("active");
            }
        }
    });

    if (scrollPos >= ($("#home").outerHeight() - $(".navbar").outerHeight())) {
        $(".navbar").addClass("active2");
    } else {
        $(".navbar").removeClass("active2");
    }
};
function calendarKeywordToggle() {
    $(".resources-name").each(function () {
        if($(this).is(':checked')) {
            $("#" + $(this).attr("value") + "_a").prop("disabled", false);
            $("#" + $(this).attr("value") + "_r").prop("disabled", false);
        } else {
            $("#" + $(this).attr("value") + "_a").prop("disabled", true);
            $("#" + $(this).attr("value") + "_r").prop("disabled", true);
        }
    });
};
function getSubmissionLink() {
    // get the curent submission link with get request values of form calendar-form
    var form = $("#calendar-form");
    var formData = form.serialize();
    var formAction = form.attr("action");

    $("#submission-link").attr("value", "https://cpcalendar.pythonanywhere.com" + formAction + "?" + formData);
};

$(document).ready(function () {
    $(window).scroll(function () {

        navCollaps();
        navActivationToggle();
        getSubmissionLink();

    });

    navCollaps();
    navActivationToggle();
    calendarKeywordToggle();
    getSubmissionLink();

    $(".hamburger").click(navToggle);

    $(".container").each(function () {
        $(this).click(navCollaps);
    });

    $("#submission-link").click(getSubmissionLink);

    $(".resources-name").each(function () {
        $(this).click(calendarKeywordToggle);
        $(this).click(getSubmissionLink);
    });

});

