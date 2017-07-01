/*fixed nav menu animations*/
$(document).ready(function(){


});




	courses_index = 1;
	exams_index = 1;
	dip_index = 1;
	stud_index = 1;




$(window).keypress(function(ev) {
	isEventHappend = false;



	/*Мои курсы*/

	$(".courses_note").keypress(function(e) {
		if (e.keyCode == 13) {
			if (!isEventHappend) {
			$("#courses_data").attr('class', 'fixed_div');
			$("#courses_data").append('<p id="courses_index_' + courses_index + '""><input type="text" class="post" name="courses_note' + courses_index + '" id="data' + courses_index + '" value="' + $("#courses_note_" + courses_index).val() + '"><a href="javascript:$(\'#courses_index_' + courses_index + '\').remove()"> X <\/a>' + '<\/p>');
			courses_index += 1;
			$("#courses").html('<p class="courses_note_' + courses_index + '"><\/p>');
			$('.courses_note_' + courses_index).html('<p><input type="text" size="20" id="courses_note_' + courses_index + '" class="courses_note" placeholder="Write here and press Enter"></p>').find('input').focus();
			isEventHappend = true;
		}};
	});

	/* Экзамены*/

	$(".exams_note").keypress(function(e) {
		if (e.keyCode == 13) {
			if (!isEventHappend) {
			$("#exams_data").attr('class', 'fixed_div');
			$("#exams_data").append('<p id="exams_index_' + exams_index + '""><input type="text" class="post" name="exams_note' + exams_index + '" id="data' + exams_index + '" value="' + $("#exams_note_" + exams_index).val() + '"><a href="javascript:$(\'#exams_index_' + exams_index + '\').remove()"> X <\/a>' + '<\/p>');
			exams_index += 1;
			$("#exams").html('<p class="exams_note_' + exams_index + '"><\/p>');
			$('.exams_note_' + exams_index).html('<p><input type="text" size="20" id="exams_note_' + exams_index + '" class="exams_note" placeholder="Write here and press Enter"></p>').find('input').focus();
			isEventHappend = true;
		}};
	});




});  

function disable_inputs() {
	$("#student_note_1").attr("disabled","");

}



	



