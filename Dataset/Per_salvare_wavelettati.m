
for ch = 1:19
    
    [c1, c2, c3, c4, c5] = get_matrices(ch, 16, ALLEEG);

    save(append('Matrici_wavelettati/ch',string(ch),'_c1'),c1)
    save(append('Matrici_wavelettati/ch',string(ch),'_c2'),c2)
    save(append('Matrici_wavelettati/ch',string(ch),'_c3'),c3)
    save(append('Matrici_wavelettati/ch',string(ch),'_c4'),c4)
    save(append('Matrici_wavelettati/ch',string(ch),'_c5'),c5)
end


