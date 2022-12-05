


sourceFolder = cd

dataFiles = listFilesOfType(sourceFolder,'.csv')

pptNum = 1;


splitByCols = {'Condition','Speed'}

vocalCond = {};
speedCond = {};
PPTNum    = [];
numCorrect= [];
numCompleted=[];
files={};

for fileRef=1:length(dataFiles)

    [p,n,e]=fileparts(dataFiles{fileRef});

    currData = readtable(dataFiles{fileRef});

    
    % Turn the string (True/False) into 1.0 and 0.0

    % Wierdly some answers are "True" and some "TRUE", perhaps some users
    % have used a different version of psychopy?
    
    correctAns1 = ismember(currData.correctClick,'True');
    correctAns2 = ismember(currData.correctClick,'TRUE')

    currData.correctAns = or( correctAns1, correctAns2);

    % identify rows with trials

    hits = ~isnan(currData.fileblock);

    currData = currData(find(hits),:);

    disp(fileRef)
    disp(dataFiles{fileRef})
    size(currData)
    condCols    = strmatch(splitByCols{1},currData.Properties.VariableNames);
    condCols(2) = strmatch(splitByCols{2},currData.Properties.VariableNames);

    uniqueConds = unique(currData(:,condCols),'rows');

    for condRef=1:size(uniqueConds,1)
        condHit1 = ismember(currData.(splitByCols{1}),uniqueConds{condRef,1});
        condHit2 = ismember(currData.(splitByCols{2}),uniqueConds{condRef,2});
        
        % Store the values
        vocalCond{end+1,1}    = uniqueConds{condRef,1}{1};
        speedCond{end+1,1}    = uniqueConds{condRef,2}{1};
        PPTNum(end+1,1)       = fileRef;
        rows                  = find(condHit1 & condHit2);

        numCorrect(end+1,1)   = sum(currData.correctAns(rows));
        numCompleted(end+1,1) = length(rows);

        files{end+1,1} = n;
    end

end

allData = table(PPTNum, vocalCond, speedCond,numCorrect, numCompleted, files);
writetable(allData, [sourceFolder '\merged\totalsOnEachCond.csv']);

whichDV = 'numCorrect'

% For each participant can we divide by the no music scores?

uPPT = unique(allData.PPTNum)


for pptNum=1:length(uPPT)
    pptHit = allData.PPTNum==uPPT(pptNum)

    justPPT = allData(pptHit,:)
    
    controlRow = ismember(justPPT.speedCond,'silent');

    justPPT.controlRelScores = zeros(size(justPPT,1),1)
    
    switch whichDV
    case 'numCompleted'
        justPPT.controlRelScores(find(~controlRow)) = justPPT.numCompleted(find(~controlRow))./justPPT.numCompleted(find(controlRow));
    case 'numCorrect'
        justPPT.controlRelScores(find(~controlRow)) = justPPT.numCorrect(find(~controlRow))./justPPT.numCorrect(find(controlRow));        
    end


    justPPT(controlRow,:) = [];

    if pptNum==1
        controlRelativeData = justPPT;
    else
        controlRelativeData = [controlRelativeData;justPPT];
    end
end


writetable(controlRelativeData, [sourceFolder '\merged\controlRelativeOnEachCond.csv']);

% data stored with correct formatting for our withihn subjects design.
%
% I have better ways of doing this, i.e. a function that already does it,
% but it's not "standard" matlab, so I'm doing it a clunky way.

active_instrumental = zeros(length(uPPT),1);
calm_instrumental   = zeros(length(uPPT),1);
active_vocals       = zeros(length(uPPT),1);
calm_vocals         = zeros(length(uPPT),1);

colNames = {'active_instrumental','calm_instrumental','active_vocals','calm_vocals'}
colToFind = {{'active','instrumental'},{'calm','instrumental'},{'active','vocals'},{'calm','vocals'}}

withinSSANOVAdata   = table(uPPT, active_instrumental, calm_instrumental, active_vocals, calm_vocals)

% Now we need to go through the dataset and find each matchign value

eachFilename = {};

for pptIndx = 1:length(uPPT)
    pptHit = controlRelativeData.PPTNum==uPPT(pptIndx)
    for eachCondIndx = 1:length(colToFind)
        condHit = ismember(controlRelativeData.speedCond,colToFind{eachCondIndx}{1}) & ismember(controlRelativeData.vocalCond,colToFind{eachCondIndx}{2})

        currHit = find(pptHit & condHit)

        if isempty(currHit)
            currVal = nan;
        else
            currVal = controlRelativeData.controlRelScores(currHit);
        end

        pptRow = find(withinSSANOVAdata.uPPT==uPPT(pptIndx))
        withinSSANOVAdata.(colNames{eachCondIndx})(pptRow) = currVal;
    end
    eachFilename{pptRow} = unique({controlRelativeData.files{pptHit}});
end
withinSSANOVAdata.filename = eachFilename'
writetable(withinSSANOVAdata, [sourceFolder '\merged\controlRelativeOnEachCondWithinSSformat_' whichDV '.csv']);

