# Frame Range Splitter

A Blender add-on for splitting an animation render across multiple computers on a home or small-office network.

## The problem

Rendering an animation on one machine is slow. If you have five PCs sitting around, you can split the work: PC 1 renders frames 1–50, PC 2 renders 51–100, and so on.

Blender has no built-in feature for this. Doing it by hand means calculating each machine's frame range yourself and typing it in on every PC. It's tedious and easy to get wrong, and a mistake means either dropped frames or the same frames rendered twice.

I hit this making a short film. The final render was over 2,000 frames split across 10–25 lab machines, and I tracked which segments were done and which came back wrong in a spreadsheet. This add-on is that process automated.

## What it does

Adds a panel to Blender's Render Properties with three inputs:

- Total frame range — defaults to the scene's current range
- Number of computers — how many machines you're splitting across
- This computer's number — which machine this one is

Press the button and the add-on sets that machine's frame range automatically.

## How to use it

1. Install the add-on on every machine
2. Copy the same `.blend` file to each one
3. On each machine, set **This computer's number** to a different value
4. Hit render

Each machine renders only its assigned slice.

## Design notes

**Nothing is written to disk.** The add-on changes the frame range in memory only — it doesn't generate separate files per machine or modify the saved `.blend`. One file stays the source of truth, so you can edit the scene once and re-copy without ending up with five diverging versions.

**Uneven splits are handled.** When the frame count doesn't divide evenly across machines, the remainder is distributed one frame at a time across the first few machines rather than dumped on the last one. No frames are dropped and none are rendered twice.

## Installation

1. Download `frame_range_splitter.py`
2. In Blender, go to Edit → Preferences → Add-ons → Install
3. Select the file and enable the checkbox
4. The panel appears under Properties → Render

## Scope

Deliberately small. This handles frame range assignment only. It does not do:

- File transfer between machines
- Job queuing
- Load balancing across machines of different speeds

Those are possible extensions.

## Built with

Python, Blender `bpy` API.
