$(function(){
    $("#form-register").validate({
        rules: {
            password : {
                required : true,
            },
            confirm_password: {
                equalTo: "#password"
            }
        },
        messages: {
            username: {
                required: "Please provide an username E.g sirajzia"
            },
            email: {
                required: "Please provide an email"
            },
            password: {
                required: "Please provide a password E.g Qwerty!@#"
            },
            schlnme: {
                required: "Please provide a school name E.g Jinnah Colleges Mansehra."
            },
            shortname: {
                required: "Please provide School short name e.g PIPS,JCM,MPS,APS etc"
            },
            address: {
                required: "Please provide school address E.g Jinnah Colleges Near Butt Pull Mansehra"
            },
            contactno: {
                required: "Please provide Official contact number"
            },
            mobno: {
                required: "Please provide Mobile number (optional)"
            },
            phnno: {
                required: "Please provide Phone number (If any)"
            },
            district: {
                required: "Please Select District"
            },
            tehsil: {
                required: "Please Select Tehsil"
            },

            confirm_password: {
                required: "Please provide a password",
                equalTo: "Please enter the same password"
            }
        }
    });
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        // enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : '<i class="zmdi zmdi-arrow-right"></i>',
            // finish : '<i class="zmdi zmdi-arrow-right"></i>',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            var username = $('#username').val();
            var email = $('#email').val();
            var schlnme = $('#schlnme').val();
            var shortname = $('#shortname').val();
            var address = $('#address').val();
            var contactno = $('#contactno').val();
            var mobno = $('#mobno').val();
            var phnno = $('#phnno').val();
            var district = $('#district').val();
            var tehsil = $('#tehsil').val();

            $('#username-val').text(username);
            $('#email-val').text(email);
            $('#schlnme-val').text(schlnme);
            $('#shortname-val').text(shortname);
            $('#address-val').text(address);
            $('#contactno-val').text(contactno);
            $('#mobno-val').text(mobno);
            $('#phnno-val').text(phnno);
            $('#district-val').text(district);
            $('#tehsil-val').text(tehsil);

            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
        }
    });
});
