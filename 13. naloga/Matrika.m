function A = Matrika(n)
  vrednost = zeros(n);
  for i = 1:n;
    for j = 1:n;
      vrednost(i,j) = randi([-5 5], 1, 1);
  end
  A = vrednost;
end