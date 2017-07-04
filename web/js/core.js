/*fixed nav menu animations*/
$(document).ready(function(){});


	courses_index = 1;





$(window).keypress(function(ev) {
	isEventHappend = false;



// для связки с backend

	// $(".courses_note").keypress(function(e) {
	// 	if (e.keyCode == 13) {
	// 		if (!isEventHappend) {
	// 		$("#courses_data").attr('class', 'fixed_div');
	// 		$("#courses_data").append('<p id="courses_index_' + courses_index + '""><input type="text" class="post" name="courses_note' + courses_index + '" id="data' + courses_index + '" value="' + $("#courses_note_" + courses_index).val() + '"><a href="javascript:$(\'#courses_index_' + courses_index + '\').remove()"> X <\/a>' + '<\/p>');
	// 		courses_index += 1;
	// 		$("#courses").html('<p class="courses_note_' + courses_index + '"><\/p>');
	// 		$('.courses_note_' + courses_index).html('<p><input type="text" size="20" id="courses_note_' + courses_index + '" class="courses_note" placeholder="Write here and press Enter"></p>').find('input').focus();
	// 		isEventHappend = true;
	// 	}};
	// });


	});




});  

function disable_inputs() {
	$("#student_note_1").attr("disabled","");

}



	



