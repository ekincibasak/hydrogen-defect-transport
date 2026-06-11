# How to Compile Your Overleaf Document

## Quick Start (Recommended - Overleaf Online)

### Step 1: Upload to Overleaf
```
1. Visit https://www.overleaf.com
2. Click "New Project" 
3. Select "Upload Project"
4. Upload the file: hydrogen_defect_transport_report.tex
```

### Step 2: Add Figures
```
1. In Overleaf, click "Files" (left sidebar)
2. Click "Upload Files" button
3. Navigate to your figures/ directory
4. Select all .png files:
   - energy_spectrum_day1.png
   - ipr_values_day1.png
   - most_localized_state_day1.png
   - defects_vs_ipr_day1.png
   - defect_strength_vs_transport_day1.png
   - defect_density_vs_mean_ipr_day3.png
   - clustering_index_vs_transport_day3.png
   - defect_strength_vs_transport_day3.png
   - notebook4_actual_vs_predicted.png
   - notebook4_feature_importance_full.png
   - notebook4_feature_importance_reduced.png
5. Click "Open" to upload all files
```

### Step 3: Compile
```
1. Click the green "Recompile" button at the top
2. Wait 10-30 seconds for PDF generation
3. View PDF in right panel
4. Click "Download PDF" to save
```

---

## Local Compilation (Mac/Linux)

### Prerequisites
Install LaTeX (MacTeX for Mac):
```bash
# Mac - using Homebrew
brew install --cask mactex

# Or download from https://www.tug.org/mactex/
```

### Compilation Steps
```bash
# Navigate to your project directory
cd /Users/basak/Desktop/IBM_quantum/

# Make sure figures are in subdirectory
mkdir -p figures
# Copy all .png files to figures/ directory

# Compile
pdflatex hydrogen_defect_transport_report.tex

# Compile again (for references to update)
pdflatex hydrogen_defect_transport_report.tex

# View the PDF
open hydrogen_defect_transport_report.pdf
```

---

## Complete Directory Structure

Before compiling, ensure your directory looks like this:

```
/Users/basak/Desktop/IBM_quantum/
│
├── hydrogen_defect_transport_report.tex    ← MAIN FILE
├── DOCUMENT_GUIDE.md                       ← What's in the document
├── COMPILATION_INSTRUCTIONS.md             ← This file
│
├── figures/                                ← CRITICAL: Create this folder
│   ├── energy_spectrum_day1.png
│   ├── ipr_values_day1.png
│   ├── most_localized_state_day1.png
│   ├── defects_vs_ipr_day1.png
│   ├── defect_strength_vs_transport_day1.png
│   ├── defect_density_vs_mean_ipr_day3.png
│   ├── clustering_index_vs_transport_day3.png
│   ├── defect_strength_vs_transport_day3.png
│   ├── notebook4_actual_vs_predicted.png
│   ├── notebook4_feature_importance_full.png
│   └── notebook4_feature_importance_reduced.png
│
├── data/
├── notebooks/
├── results/
└── README.md
```

---

## Common Issues & Solutions

### Issue 1: "Package graphicx not found"
**Solution:** This is normal - Overleaf handles this automatically.  
Locally, ensure all LaTeX packages are installed:
```bash
# Mac
brew install mactex-no-gui
```

### Issue 2: "Image not found" errors
**Solution:** Make sure all .png files are in the `figures/` subdirectory.  
Update the file paths in LaTeX:
```latex
% In the document, images should be referenced as:
\includegraphics[width=0.8\textwidth]{figures/energy_spectrum_day1.png}
```

### Issue 3: PDF too large
**Solution:** This is normal (30-40 MB with all plots).  
Reduce figure resolution or compress PDF after generation:
```bash
# Compress PDF on Mac
sips -Z 50% *.pdf
```

### Issue 4: References not updating
**Solution:** Compile twice:
```bash
pdflatex hydrogen_defect_transport_report.tex
pdflatex hydrogen_defect_transport_report.tex
```

---

## Expected Output

### File Size
- **Main PDF:** 30-40 MB (due to high-resolution figures)
- **Pages:** 25-30 pages
- **Compilation time:** 30-60 seconds

### PDF Contents
- Professional title page
- Abstract
- 8 major sections
- 11 figures with captions
- 4 tables
- References section
- Appendices

---

## Overleaf vs Local Compilation

| Feature | Overleaf | Local |
|---------|----------|-------|
| **Setup** | Instant | Need LaTeX |
| **Collaboration** | Easy sharing | Need git |
| **Speed** | Fast (cloud) | Faster (local) |
| **Cost** | Free tier available | Free |
| **Recommended** | ✅ For IBM submission | For development |

---

## For IBM Quantum Submission

Once compiled, your PDF includes:

1. ✅ Complete theoretical framework
2. ✅ All experimental results
3. ✅ 11 scientific figures
4. ✅ Detailed interpretations
5. ✅ Quantum computing context
6. ✅ Future directions
7. ✅ Reproducibility information

**Ready to submit!**

---

## Advanced: Custom LaTeX Compilation

If you need full control, use this advanced script:

```bash
#!/bin/bash
cd /Users/basak/Desktop/IBM_quantum/

# Clean previous builds
rm -f *.pdf *.aux *.log *.out *.toc

# Compile with verbose output
pdflatex -interaction=nonstopmode \
         -file-line-error \
         -shell-escape \
         hydrogen_defect_transport_report.tex

# Check for errors
if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi

# Second pass (for references)
pdflatex -interaction=nonstopmode \
         hydrogen_defect_transport_report.tex

echo "✓ Compilation complete!"
open hydrogen_defect_transport_report.pdf
```

Save this as `compile.sh` and run:
```bash
chmod +x compile.sh
./compile.sh
```

---

## Quality Checklist Before Submission

After compilation, verify:

- ✅ All 11 figures appear correctly
- ✅ Table of contents shows all sections
- ✅ Page numbers are correct
- ✅ Math equations render properly
- ✅ Hyperlinks work (test in PDF viewer)
- ✅ Fonts are consistent
- ✅ Figure captions are readable
- ✅ No blank pages or missing content
- ✅ PDF file is not corrupted
- ✅ File size is reasonable

---

## Next Steps After Compilation

1. **Review the PDF** for visual quality
2. **Check all figures** are clear and properly positioned
3. **Verify equations** render correctly
4. **Test hyperlinks** in PDF viewer
5. **Add any IBM-specific** information if needed
6. **Upload to IBM** submission portal

---

## Support Resources

If you encounter issues:

1. **Overleaf Help:** https://www.overleaf.com/help
2. **LaTeX Issues:** https://www.latex-project.org/help/documentation/
3. **Common Errors:** Search the specific error message

---

**Document Ready:** ✅ hydrogen_defect_transport_report.tex  
**Status:** Professional-quality academic document  
**Target:** IBM Quantum submission  
**Compilation Time:** < 1 minute  

Good luck with your IBM submission! 🚀
