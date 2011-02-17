% http://www.craigmurphy.com/blog/?p=1417
function dia(n)
	a = zeros(1+n-'A') + ' ';
	for c = 'A':n
		a(1+c-'A',1+c-'A') = c;
	endfor

	a = [a fliplr(a)(:,2:size(a)(2))];
	a = [flipud(a); a(2:size(a)(1),:)];
	a = a';

	% Print
	for n = 1:size(a)(1)
		printf([a(n,:) '\n']);
	endfor
endfunction
