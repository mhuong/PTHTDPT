aphex = audioread('FormulaSnippet.wav');
mono = (aphex(:,1) + aphex(:,2))/2;
spectrogram(mono,1024,120,2048,'power','yaxis');
set(gca,'YScale','log');
colormap('winter');
xlabel('Time')
ylabel('Frequency (Log Scale)')