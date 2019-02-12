function matrika = narascajoca(n)
  vrednost = ones(n);
  for i = 1:n;
    for j = 1:n;
      vrednost(i,j) = i + j - 1;
  end
  matrika = vrednost;
end