$(function() {
	$('#btnSearch').click(function() {
		$.ajax({
			url: '/search',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
				console.log(response);
			},
		});
	});
});
