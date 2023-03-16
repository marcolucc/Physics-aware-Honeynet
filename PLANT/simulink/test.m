% Set the time interval for clearing the SDI (in seconds)
timeInterval = 5 * 60 * 60; % 5 hours in seconds

% Load the Simulink model
model = 'plc.slx';
sim(model);

% Create a timer object to clear the SDI every 5 hours
t = timer('Period', timeInterval, 'ExecutionMode', 'fixedRate', 'TimerFcn', {@clearSDI, model});

% Start the timer
start(t);

% Function to clear the SDI and restart the Simulink model
function clearSDI(~, ~, model)
    % Clear the SDI
    Simulink.sdi.clear;
    % Close the Simulink model
    bdclose(model);
    % Restart the Simulink model
    sim(model);
end
